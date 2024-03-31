import { error, json } from '@sveltejs/kit';
import { getXataClient } from '../../../xata';

export const POST = async ({ locals, request }) => {
    const user = await locals.auth();

    if (!user) error(401);

    const parse = await request.json();
    console.log(parse); // { code: 'TEST', number: 3 }

    const parse2 = JSON.stringify(parse); // '{"code":"TEST","number":3}'
    console.log(parse2);

    const { response } = await fetch('https://brebeufapi-nayy.vercel.app/api/besthexes', {
        method: 'POST',
        headers: { 'Content-type': 'text/html' },
        body: parse2 // Send the JSON string as the request body
    }).then((res) => res.json());
    return json(response);	
};