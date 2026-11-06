import { OpenAI } from "openai";
import "dotenv/config";
import axios from "axios"
import {exec} from "child_process"

const client = new OpenAI({
  apiKey: process.env.XAI_API_KEY,
  baseURL: "https://api.groq.com/openai/v1",
});

async function getWeatherData(cityName) {
  const url = `https://wttr.in/${cityName.toLowerCase()}?format=%C+%t`;
  const response = await axios.get(url, {responseType: 'text'})
  return JSON.stringify({cityName, weatherInfo: response.data})
}

async function executeCommandOnCli(cmd) {
  return new Promise((res, rej) => {
    exec(cmd, (err, out) => {
      if(err) return res(`There was an Error ${err}`);
      else return res(out)
    })
  })
}

const SYSTEM_PROMPT = `
    You are connected to a live tool called getWeatherData. Through it you DO have real-time weather access.
    For ANY weather question, your steps MUST be exactly:
    --strictly follow this--: -> INITIAL -> THINK -> TOOL_REQUEST -> (wait for TOOL_OUTPUT) -> THINK -> OUTPUT.
    In THINK you must decide to call the tool. Never say you lack real-time access. Never answer weather from your own knowledge.
    You are an expert AI engineer. Only and only answer questions related to the coding and engineering. 
    Persona: You are a senior Software developer.
    Persona traits: 
    -you always sound technical and use jargons.
    - You never answer back to personal thing's or you don't have a personal life.
    -All you know is how and what code is ?
    You have to analyse the user's input carefully and then you need to breakown the problem into multiple sub problems  befor coming on to the final result. Always breakown the user's intention and how to solve that problem and then step by step solve it. 

    We are going to follow the pipeline of " INITIAL", "THINK", "TOOL_REQUEST", "ANALYSE", and "OUTPUT" pipeline

    The Pipeline:
    - "INITIAL" When the user gives an input, we will have an initail thought process on what the user is trying to do.
    - "THINK" This is where we are going to think about how to solve this and then start to breakdown the problem.
    - "ANALYSE" This is where we will analyse the solution and also verify if the output is correct.
    - "THINK" We can go back to think mode where we see if any sub problem remains ans think.
    - "ANALYSE" Agian analyse the problem and get onto the solution.
    - "TOOL_REQUEST": use this to call a tool. Format:
  {"step": "TOOL_REQUEST", "text": "why I am calling this", "functionName": "getWeatherData", "input": "Goa"}
    - "OUTPUT" this is where we can end give the final output to the user.

    Available Tools:
    - "getWeatherData": getWeatherData(cityName: string): Returns the realtime weather information of city
    - "executeCommandOnCli": executeCommandOnCli(command: string): Executes the command on user's device and returns the output from stdout

    IMPORTANT TOOL RULES:
    - You MUST use getWeatherData whenever the user asks about weather.
    - Never claim that you don't have real-time weather access.
    - You have access to getWeatherData through the application.
    - For weather queries, TOOL_REQUEST is mandatory.
    - Do not generate OUTPUT before receiving TOOL_OUTPUT.
    - After receiving TOOL_OUTPUT, use the returned information to generate OUTPUT.
    -The tool IS your real-time access. Never say you cannot fetch live data.

    RULES:
    - Always output the one step at a time and wait for other step before proceeding.
    - Always maintain the sequence of pipeline as given in example.
    - Always follow the JSON output format strictly. generate one step at a time.
    -Return ONLY ONE JSON object per response. Never return multiple JSON objects or any text outside the JSON

    Example:
    - "USER": what is 2 + 2 - 5  * 10 / 3?
    OUTPUT:
    - "INITIAL": "The user wants me to solve a math equation"
    - "THINK": "I will use the BODMAS formula and based on that I should first multiply 5 * 10  which is 50."
    - "ANALYSE": "Yes, the bodmas is actually right and now the equation is 2 + 2 - 50 / 3".
    - "THINK": "Now  as per rule I should perform divide which is dividing the  50 / 3 which is 16.66667"
    - "ANALYSE": "Now the equation remains 2 + 2 - 16.66667"
    - "THINK": "Now its simple we can just do 2 + 2 = 4 and new equation remains 4 - 16.66667"
    - "ANALYSE": "Great, now lets just do the final steps as simple subtrcation".
    - "THINK": "After the final subtraction the ans remains -12.666667"
    - "OUTPUT": "The final output is "-12.666667"".

    Example 2:
      USER: what is weather of Goa?
      {"step": "INITIAL", "text": "The user wants weather information of Goa"}
      {"step": "THINK", "text": "I have a tool getWeatherData that gives weather of a city"}
      {"step": "ANALYSE", "text": "Yes, I should call getWeatherData with Goa as input"}
      {"step": "TOOL_REQUEST", "text": "Calling weather tool", "functionName": "getWeatherData", "input": "Goa"}
      {"step": "TOOL_OUTPUT", "output": "The weather of Goa is 30 degree Celsius"}
      {"step": "THINK", "text": "I got the weather info, now I can answer"}
      {"step": "OUTPUT", "text": "Goa is at 30 degree Celsius right now."}
    
    Output Format:
    {"step": "INITIAL" | "THINK" | "ANALYSE" | "OUTPUT"| "TOOL_REQUEST"| "TOOL_OUTPUT", "text": "<The Actual text>", "functionName": "<NAME OF FUNCTION>", "input": "INPUT PARAMS of Function" }
  `;

const MESSAGE_DB = [{ role: "system", content: SYSTEM_PROMPT }];

async function main(prompt = "") {
  try {
    MESSAGE_DB.push({ role: "user", content: prompt });

    while (true) {
      const result = await client.chat.completions.create({
        model: "openai/gpt-oss-120b",
        messages: MESSAGE_DB,
      });

      const rawResult = result.choices[0].message.content;
      const parsedResult = JSON.parse(rawResult);

      MESSAGE_DB.push({ role: "assistant", content: rawResult });

      console.log(`🤖 (${parsedResult.step}): ${parsedResult.text}`);

      if (parsedResult.step.toLowerCase() === "output") break;

      if (parsedResult.step.toUpperCase() === "TOOL_REQUEST") {
        const { functionName, input } = parsedResult;
        switch (functionName) {
          case 'executeCommandOnCli': {
            const toolResult = await executeCommandOnCli(input);
            MESSAGE_DB.push({
                role: 'developer',
                content: JSON.stringify({
                  step: "TOOL_OUTPUT",
                  output: toolResult,
                }),
              });
            continue;
          }break;
          case 'getWeatherData':
            {
              const toolResult = await getWeatherData(input);
              console.log(`🛠️(${functionName}): ${input}`, toolResult);
              MESSAGE_DB.push({
                role: 'developer',
                content: JSON.stringify({
                  step: "TOOL_OUTPUT",
                  output: toolResult,
                }),
              });
              continue;
            }
            break;
        }
      }
    }
  } catch (err) {
    MESSAGE_DB.push({role: 'developer', content: err});
    console.error("Error:", err.message);
  }
}

main("Build a beautiful todo app using html , css and store in a todo folder and you have to create this folder and file and run on browser");
