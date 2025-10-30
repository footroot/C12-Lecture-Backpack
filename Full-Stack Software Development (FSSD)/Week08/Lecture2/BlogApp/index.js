import express from "express";
import mongoose from "mongoose";
import router from "./routes/index.js";

const app = express();

app.use(express.json())

// MongoDB Connection
const uri =
  "mongodb+srv://danw:luXIEW0TZtzHvy85@cluster0.wkxjt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const clientOptions = {
  serverApi: { version: "1", strict: true, deprecationErrors: true },
};

mongoose
  .connect(uri, clientOptions)
  .then(() => {
    console.log("Connected to MongoDB Successfully");
  })
  .catch((error) => {
    console.log(error);
  });

app.listen(8080, () => {
  console.log("Server is running on http://localhost:8080");
});


app.use('/', router)