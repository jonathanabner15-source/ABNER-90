console.log('System online')

const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Express online, Jonathan'));
app.listen(3000, () => console.log('Server running on port 3000'));
