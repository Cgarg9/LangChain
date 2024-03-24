import OpenAI from 'openai';
import express from 'express';
import path from 'path';
import 'dotenv/config'
import { fileURLToPath } from 'url';

const secretKey = process.env.OPENAI_API_KEY;
// console.log(secretKey);
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const openai = new OpenAI({
    apiKey: secretKey,
})

const messages = [];
async function main(input) {
    messages.push({ role: 'user', content: input });
    console.log(messages);
    const completion = await openai.chat.completions.create({
        messages: messages,
        model: 'gpt-3.5-turbo'
    });
    return completion.choices[0]?.message?.content;
}
// main("hi")

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, './index.html'));
});

app.post('/api', async function (req, res, next) {
    console.log(req.body);
    const output = await main(req.body.input);
    res.json({ success: true, message: output });
});

app.listen(process.env.PORT, () => {
    console.log(`listening on port ${process.env.PORT}`);
})