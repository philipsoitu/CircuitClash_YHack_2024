import { error, json } from '@sveltejs/kit';
import { getXataClient } from '../../../xata';

export const POST = async ({ locals, request }) => {
	const user = await locals.auth();

	if (!user) error(401);

	const parse = await request.json();
	console.log(parse);

	let parse2 = JSON.stringify(parse);
	console.log(parse2);
	console.log(typeof parse2);
	const { response } = await fetch('https://brebeufapi.vercel.app/api/besthexes', {
		method: 'POST',
		headers: { 'Content-type': 'text/html'},
		body: parse
	}).then((res) => res.json());

	return json(response);
};
