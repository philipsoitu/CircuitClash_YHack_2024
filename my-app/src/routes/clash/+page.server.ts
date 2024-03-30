import {  superValidate } from "sveltekit-superforms";
import { schema } from "./schema";
import { error,fail, redirect } from "@sveltejs/kit";
import { zod } from "sveltekit-superforms/adapters";

export const load = async () => {

	return {
		form: await superValidate(zod(schema))
	};
};

export const actions = {
	default: async ({request}) => {
		const form = await superValidate(request, zod(schema));

		if (!form.valid) {
			return fail(400, { form });
		}

        const { hexes } = await fetch('https://brebeufapi.vercel.app/api/besthexes', {
					method: 'POST',
					headers: { 'Content-type': 'text/html' },
					body: JSON.stringify(form.data)
				}).then((res) => res.json());

		

		return { form };
	}
};
