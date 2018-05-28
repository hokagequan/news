import {Router} from 'express';

let router = Router();

router.route('/')
	.get((req, res) => {
		res.send("Hello");
	});

export default router;