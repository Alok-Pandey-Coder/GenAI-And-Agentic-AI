import {OpenAI} from "openai"
import "dotenv/config"

const client = new OpenAI({
  apiKey: process.env.XAI_API_KEY,
  baseURL: 'https://api.groq.com/openai/v1',
});

async function main() {
   try {
    const result = await client.chat.completions.create({
      model: 'openai/gpt-oss-120b',
      messages: [{role: 'user', content:
         `tell me what is 2 + 2 equals?
          Do not add anything else in ans, take the samples from examples.
          Examples:
          - what is 5 + 9 equals?
            Expected: 14 (Fourteen).
          - what is 3 + 17 equals ?
            Expected: 20 (Twenty).
         `}],
    });

    console.log(`Ans from Gemini Api: `, result.choices[0].message.content);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

main();
