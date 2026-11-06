import { OpenAI } from "openai";
import "dotenv/config";

const client = new OpenAI({
  apiKey: process.env.XAI_API_KEY,
  baseURL: "https://api.groq.com/openai/v1",
});

const SYSTEM_PROMPT = `
  You are an expert AI engineer. You have to analyse the user's input carefully and then you need to breakown the problem into multiple sub problems  befor coming on to the final result. Always breakown the user's intention and how to solve that problem and then step by step solve it. 

  We are going to follow the pipeline of " INITIAL", "THINK", "ANALYSE", and "OUTPUT" pipeline

  The Pipeline:
  - "INITIAL" When the user gives an input, we will have an initail thought process on what the user is trying to do.
  - "THINK" This is where we are going to think about how to solve this and then start to breakdown the problem.
  - "ANALYSE" This is where we will analyse the solution and also verify if the output is correct.
  - "THINK" We can go back to think mode where we see if any sub problem remains ans think.
  - "ANALYSE" Agian analyse the problem and get onto the solution.
  - "OUTPUT" this is where we can end give the final output to the user.

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
  
  Output Format:
  {"step": "INITIAL" | "THINK" | "ANALYSE" | "OUTPUT", "text": "<The Actual text>" }
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

      const rawResult = result.choices[0].message.content
      const parsedResult = JSON.parse(rawResult)

      MESSAGE_DB.push({role: 'assistant', content: rawResult})

      console.log(`🤖 (${parsedResult.step}): ${parsedResult.text}`)

      if(parsedResult.step.toLowerCase() === 'output') break;
    }

  } catch (err) {
    console.error("Error:", err.message);
  }
}

main("What is the weather of noida ?");
