import type { PageServerLoad } from './$types';
import { getXataClient } from '../xata';
import { redirect } from '@sveltejs/kit';
import { User } from 'tabler-icons-svelte';

export const load: PageServerLoad = async ({locals}) => {

	
    let user = await locals.auth();

    // Check if the user already exists in the database
    const existingUser = await getXataClient().db.users.filter({
        email: user?.user?.email,
    }).getFirst(); // Use getFirst() to attempt to fetch a single user record

    // If the user doesn't exist, create a new user record
    if (!existingUser) {
        await getXataClient().db.users.create({
            email: user?.user?.email,
            levelnumber: 1,
        });
    }
	
	const level = await getXataClient().db.users.filter({
        email: user?.user?.email,
    }).getFirst();
	const questions = await getXataClient().db.questions.getAll();

    return {
    	questions,level
    };

};
