import express from 'express';
import OpenAI from 'openai';
import dotenv from 'dotenv';
dotenv.config();

const app = express();
const port = process.env.PORT || 8000;

// configure openAi
const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

// config middlewares
app.use(express.json());


// routes
app.post("/generateImage", async (req, res) => {
    const { prompt } = req.body;
    try {
        const imageResponse = await openai.images.generate({
            model: "dall-e-3",
            prompt,
            n: 1, // number of images
            size: "1024x1024",
        })
        res.json(imageResponse.data[0].url);
    } catch (error) {
        console.log(error.message);
        res.json({ message: "error generating image" });
    }
});

// start the server
app.listen(port, () => {
    console.log(`listening on port ${port}`);
})