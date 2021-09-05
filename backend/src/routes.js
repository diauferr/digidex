const express = require("express");
const UserController = require("./controller/UserController");
const routes = express.Router();

routes.get("/", function (req, res) {
  res.json({
    message: "Bem-vindo ao backend MongoDB da digidex.",
  });
});

routes.get("/users", UserController.index);
routes.post("/users", UserController.store);

module.exports = routes;
