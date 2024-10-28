// routes/users.js
const express = require('express');
const myTestRouter = express.Router();

// Example endpoint: Get all users
myTestRouter.get('/', (req, res) => {
    res.send('List of users');
});

// Example endpoint: Create a user
myTestRouter.post('/', (req, res) => {
    res.send('User created');
});

// Example endpoint: Get a user by ID
myTestRouter.get('/:id', (req, res) => {
    res.send(`User with ID ${req.params.id}`);
});

module.exports = myTestRouter;