import type { PageServerLoad } from './$types';
import { getXataClient } from '../xata';
import { redirect } from '@sveltejs/kit';
import { User } from 'tabler-icons-svelte';

export const load: PageServerLoad = async ({locals}) => {
    let user = await locals.auth()
    await getXataClient().db.users.create({
				email: user?.user?.email,
				levelnumber: 0
			});
			


	const questions = await getXataClient().db.questions.getAll();

	return {
		questions
	};
};
