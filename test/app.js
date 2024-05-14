const express = require('express')



const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});
app.get('/fati', (req, res) => {
  res.send('this is test');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
