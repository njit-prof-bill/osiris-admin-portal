So everyone will not be implementing their assigned API's and coding in the same file, we will factor out the API's from src/index.js, into src/routes/testApi.js

to implement your API's make a copy of src/routes/testApi.js and re name it appropriately and rename myTestRouter within testApi.js to something like "addUserRoute". Make sure you change the last line as well -> modules.exports = "..."

then once you implement your api, you now have to "import" it into src/index.js with the following code: 

const testRoutes = require('./routes/testApi');
app.use('/api/users', testRoutes);

the API endpoint is now reachable at (hostName)/api/users