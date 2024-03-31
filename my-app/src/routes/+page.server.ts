import type { PageServerLoad } from './$types';
import { getXataClient } from '../xata';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async (event) => {

	const questions = await getXataClient().db.questions.getAll();

	return {
		questions
	};
};
