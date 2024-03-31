import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async (event) => {
	const user = await event.locals.auth();
	console.log(user);

	return {
        user:user,
		loggedIn: !!user,
		email: user?.user?.email,
		avatar: user?.user?.image,
		name: user?.user?.name
	};
};
