import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { getXataClient } from '../../xata';

export const load: PageServerLoad = async (event) => {
	const session = await event.locals.auth();
	if (!session?.user) throw redirect(303, '/auth');

     const messages = await getXataClient()
				.db.questions
				.filter({ id: "1" })
				.getAll();

	return {
        messages
    };
};
