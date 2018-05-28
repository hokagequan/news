import {Router} from 'express';
import data from './data';

let router = Router();

router.use('/data/', data);

export default router;