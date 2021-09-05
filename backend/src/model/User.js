const mongoose = require("mongoose");

const dataSchema = new mongoose.Schema({
  name: String,
  password: String,
  email: String,
  createdAt: { type: Date, default: Date.now },
});

const user = mongoose.model("User", dataSchema);

module.exports = user;
