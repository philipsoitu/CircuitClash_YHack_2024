import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { getXataClient } from '../../xata';

export const load: PageServerLoad = async (event) => {
    const session = await event.locals.auth();
    if (!session?.user) throw redirect(303, '/auth');

    // Fetch the user based on the session email
    const user = await getXataClient()
        .db.users
        .filter({ email: session.user.email })
        .getFirst(); // Fetches the single user matching the email

    if (!user) {
        throw redirect(303, '/auth'); // Redirects if the user is not found
    }

    // Fetching questions where 'id' matches the user's 'levelnumber'
    const messages = await getXataClient()
        .db.questions
        .filter({ id: user.levelnumber?.toString() }) // Direct comparison, assuming 'id' and 'levelnumber' are of the same type
        .getAll();

    return { messages };
};
