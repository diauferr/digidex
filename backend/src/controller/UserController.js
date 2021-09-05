const User = require("../model/User");

module.exports = {
  async index(req, res) {
    const users = await User.find(); //select * from User
    res.json(users);
  },

  async store(req, res) {
    const { name, password, email, createdAt } = req.body;

    let createData = {};

    createData = {
      name,
      password,
      email,
      createdAt,
    };

    const users = await User.create(createData); //select * from User
    res.json(users);
  },
};
