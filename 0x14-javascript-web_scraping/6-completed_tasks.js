#!/usr/bin/node
const request = require('request');

// Check for the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

// Get the API URL from command-line argument
const apiUrl = process.argv[2];

// Make the HTTP request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching the URL:', error);
    process.exit(1);
  }

  try {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Initialize an object to count completed tasks by user ID
    const userTasks = {};

    // Iterate over todos to count completed tasks for each user
    todos.forEach(todo => {
      if (todo.completed) {
        if (!userTasks[todo.userId]) {
          userTasks[todo.userId] = 0;
        }
        userTasks[todo.userId]++;
      }
    });

    // Print the results, but only include users with completed tasks
    console.log(userTasks);
  } catch (err) {
    console.error('Error parsing JSON:', err);
    process.exit(1);
  }
});
