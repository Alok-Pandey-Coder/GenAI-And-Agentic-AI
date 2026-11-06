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
      messages: [{role: 'user', content: 'tell me story about little red ridding hood'}],
    });

    console.log(`Ans from Gemini Api: `, result.choices[0].message.content);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

main();
