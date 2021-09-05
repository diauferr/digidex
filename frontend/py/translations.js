import database from "./database.js";

function count() {
  let json = database;

  let counted = Object.keys(json).length;

  console.log(counted);
}

count()