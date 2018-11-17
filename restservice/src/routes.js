import express from 'express';

const router = express.Router();

router.get('/api', (req, res) => {
  // Response
  res.json({
    id: 1,
    response: 'Sample text',
  });
});

export default router;
