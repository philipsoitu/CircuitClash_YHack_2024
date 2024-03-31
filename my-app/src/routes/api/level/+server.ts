import { error, json } from "@sveltejs/kit";
import { getXataClient } from "../../../xata";

export const POST = async ({ locals, request }) => {
    const user= await locals.auth();

	if (!user) error(401);

	const parse = await request.json();
	if (!parse.success) error(400);

	const user2 = await getXataClient()
        .db.users
        .filter({ email: user.user?.email })
        .getFirst(); // Fetches the single user matching the email

	if(user2?.id!=undefined)
	await getXataClient().db.users.update({
        id: user2?.id,
        email:user2.email,
		levelnumber:parse.data.level
    });
	
	return json({ success: true });
};
