import { error, fail, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { getXataClient } from '../../xata';
import { zod } from 'sveltekit-superforms/adapters';
import { superValidate } from 'sveltekit-superforms/server';
import { schema } from './schema';

export const load: PageServerLoad = async ({ locals }) => {
	const user = await locals.auth();
	if (!user) throw redirect(303, '/auth');
	const level = await getXataClient().db.users.filter({ id: user?.user?.id }).getAll();
	console.log(level);
	return {
		level,
		form: await superValidate(zod(schema))
	};
};

export const actions = {
	default: async ({ request, fetch, locals }) => {
		const form = await superValidate(request, zod(schema));
        
		if (!form.valid) {
			return fail(400, { form });
		}
		const user = await locals.auth();

		const useR =  getXataClient().db.users.filter({ id: user?.user?.id }).select(["levelnumber"]);

		const messages = getXataClient().db.questions.filter({ id: useR });

		const { response } = await fetch('https://brebeufapi.vercel.app/api/besthexes', {
			method: 'POST',
			headers: { 'Content-type': 'text/html' },
			body: JSON.stringify(form.data)
		}).then((res) => res.json());

		return { form, response,messages };
	}
};
