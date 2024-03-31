<script lang="ts">
	import { superForm } from 'sveltekit-superforms';
	import { Field, Control } from 'formsnap';
	import { Label } from 'formsnap';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import type { PageData } from './$types.js';

	import CodeMirror from 'svelte-codemirror-editor';
	import { oneDark } from '@codemirror/theme-one-dark';

	import SuperDebug from 'sveltekit-superforms';
	import { onMount } from 'svelte';
	import TruthTable from './tablegenerate.svelte'
	const inputData = ['I01', 'I02'];
	const outputData = ['O01', 'O02'];
	const truthTable = [
		{'I01': 0, 'I02': 0, 'O01': 0, 'O02': 0},
		{'I01': 0, 'I02': 1, 'O01': 1, 'O02': 0},
		{'I01': 1, 'I02': 0, 'O01': 1, 'O02': 0},
		{'I01': 1, 'I02': 1, 'O01': 0, 'O02': 1}
	];
	let value = '';
</script>

<main class="container flex flex-1 flex-col overflow-hidden py-8">
	<div class="mb-4 flex items-center justify-between">
		<h1 class="h1">Multiplayer</h1>
	</div>

	<div class="grid flex-1 gap-8 overflow-hidden lg:grid-cols-3">
		<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
			<div class="my-4 flex h-full flex-col gap-4 p-4 max-w-lg">
				<div class="card">
					<h1 class="h1">What you need to do</h1>
					<p>Put</p>
					<TruthTable {inputData} {outputData} {truthTable} />				</div>
				<div class="card"></div>
			</div>
		</div>

		<div class="col-span-2 my-4 hidden rounded-xl bg-primary p-4 lg:grid overflow-y-auto">
			<CodeMirror
				bind:value
				styles={{
					'&': {
						width: '100%',
						maxWidth: '100%',
						height: '20rem'
					}
				}}
				theme={oneDark}
				placeholder={'Start coding here..'}
			/>
			<button class="btn"> Submit </button>
		</div>
	</div>
</main>
