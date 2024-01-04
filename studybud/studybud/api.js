const express = require('express');
const app = express();
const port = 3000;

// Définir une route pour l'API
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Bonjour, ceci est une API!' });
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur http://localhost:${port}`);
});
