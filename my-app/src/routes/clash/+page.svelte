<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import { Field, Control } from 'formsnap';
	import { Label } from 'formsnap';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import type { PageData } from './$types.js';

	import CodeMirror from 'svelte-codemirror-editor';
	import { oneDark } from '@codemirror/theme-one-dark';

	import { schema } from './schema.js';
	import SuperDebug from 'sveltekit-superforms';
	export let data: PageData;

	const form = superForm(data.form, {
		validators: zodClient(schema)
	});
	const { form: formData, enhance } = form;
</script>

<main class="container flex flex-1 flex-col overflow-hidden py-8">
	<div class="mb-4 flex items-center justify-between">
		<h1 class="h1">Multiplayer</h1>
	</div>

	<div class="grid flex-1 gap-8 overflow-hidden lg:grid-cols-3">
		<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
			<div class="my-4 flex h-full flex-col gap-4 p-4 max-w-lg">
				<div class="">
					<div class="card">
						<h1 class="h1">What you need to do</h1>
						<p>
							Put 
						</p>
					</div>
					<div class="card">
						<h1 class="h1">What you need to do</h1>
						<p>
							Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum mollitia alias, illum
							tempora sed maiores repellendus deserunt corrupti aperiam tempore necessitatibus.
						</p>
					</div>
				</div>
			</div>
		</div>

		<div class="col-span-2 my-4 hidden rounded-xl bg-primary p-4 lg:grid">
			<form use:enhance class="" method="POST">
				<Field {form} name="code">
					<Control let:attrs>
						<Label class="h1">Code</Label>
						<CodeMirror
							bind:value={$formData.code}
							styles={{
								'&': {
									width: '100%',
									maxWidth: '100%',
									height: '20rem'
								}
							}}
							theme={oneDark}
							placeholder={'Start coding here..  \n sdsdsd'}
						/>
					</Control>
				</Field>
			</form>
		</div>
	</div>
</main>
