const express = require("express");
const cookieParser = require("cookie-parser");
const cors = require("cors");
const path = require("path");
const routes = require("./src/routes");
const mongoose = require("mongoose");

const app = express();

mongoose.connect(
  "mongodb://localhost:27017/digidex",
  {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useFindAndModify: false,
  },
  function (err) {
    if (err) {
      console.log(err);
    } else {
      console.log("Mongodb connected successfully");
    }
  }
);

app.use(cors());
app.use(cookieParser());
app.use(express.json());
app.use(routes);
app.listen(3008, function () {
  console.log("OK");
});
