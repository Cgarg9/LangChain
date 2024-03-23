import OpenAI from 'openai';
import express from 'express';
import path from 'path';
import 'dotenv/config'
import { fileURLToPath } from 'url';
import OpenAI from 'openai';


const secretKey = process.env.OPENAI_API_KEY;
// console.log(secretKey);
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, './index.html'));
});

app.post('/api', function (req, res, next) {
    console.log(req.body);
    res.json(req.body);
});

app.listen(process.env.PORT, () => {
    console.log(`listening on port ${process.env.PORT}`);
})