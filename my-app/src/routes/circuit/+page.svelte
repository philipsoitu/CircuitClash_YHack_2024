<script lang="ts">
	import CodeMirror from 'svelte-codemirror-editor';
	import { oneDark } from '@codemirror/theme-one-dark';
	import Visualizer from '../../components/Visualizer/Visualizer.svelte';
	import SuperDebug, { superForm } from 'sveltekit-superforms';
	import { onMount } from 'svelte';
	import TruthTable from './tablegenerate.svelte';
	import { writable } from 'svelte/store';
	import { stringify } from 'postcss';

	let buttontext = ['Show Question', 'Show circuit'];
	let buttontextindex = 1;
	let description = 'Define the functionality of a full 1-bit adder in shdl.';
	let title = 'Full 1-bit Adder';
	let qnum = 1;

	export let data;

	// Assuming data.messages[0].io contains structured data you might need to separate or process further
	console.log(data.messages[0].io);
	let ioData = JSON.parse(data.messages[0].io.replace(/'/g, '"')); // Ensure this is correctly structured for parsing
	let inputData = ioData.input; // Hypothetical structure
	let outputData = ioData.output; // Hypothetical structure
	let tb = JSON.parse(data.messages[0].expectedoutput.replace(/'/g, '"')); // Ensure this is correctly structured for parsing

	console.log(inputData);
	console.log(outputData);
	console.log(tb);
	let response = '';
	let value = '';
	async function sendCode(code: string) {
		try {
			console.log(typeof code);
			let response = await fetch('/api/code', {
				method: 'POST',
				headers: {
					'Content-Type': 'text/html'
				},
				body: code // Modify this string as needed
			});

			if (response.ok) {
				const responseData = await response.json();
				console.log(response);
				if (responseData['answer'] == 'true') {
					let lvl: number = parseInt(data.messages[0].id);
					lvl++;
					updateLevel(lvl);
				}
			} else {
				console.error('Failed to process string');
			}
		} catch (error) {
			console.error('Error processing string:', error);
		}
	}

	async function updateLevel(level: number) {
		try {
			let response = await fetch('/api/message', {
				method: 'POST',
				body: JSON.stringify(level.toString()) // Modify this string as needed
			});

			if (response.ok) {
				const responseData = await response.json();
				console.log(response);
			} else {
				console.error('Failed to process string');
			}
		} catch (error) {
			console.error('Error processing string:', error);
		}
	}
	function changeText() {
		if (buttontextindex === 0) {
			buttontextindex = 1;
		} else {
			buttontextindex = 0;
		}
	}
</script>

<main class="flex justify-between rounded-2xl border-2 main px-4 py-2">
	{#if data.messages[0].type == '1'}
		<div class="grid flex-1 gap-2 lg:grid-cols-2">
			{#if buttontextindex === 1}
				<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
					<div class="card">
						<h1 class="h1">Q{data.messages[0].id}: {data.messages[0].name}</h1>
						<p class="questiondesc">{data.messages[0].description}</p>
						<TruthTable truthTable={tb} {inputData} {outputData} />
					</div>
				</div>
			{:else}
				<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
					<div class="card">
						<h1 class="h1">Circuit:</h1>
						<Visualizer width={500} height={500} shdl={value} />
					</div>
				</div>
			{/if}

			<div class="col-span-1 my-4 hidden rounded-xl bg-primary p-4 lg:grid overflow-y-auto">
				<CodeMirror
					bind:value
					styles={{
						'&': {
							width: '100%',
							maxWidth: '100%',
							height: '25em'
						}
					}}
					theme={oneDark}
					placeholder={'Start coding here..'}
				/>
				<div class="grid lg:grid-cols-2 flex-1 gap-2 mx-auto mt-2"> 
					<button 
						class="btn side-by-side-btn" 
						on:click={() => sendCode(JSON.stringify({ code: value, number: parseInt(data.messages[0].id) }))}
					>Submit</button>
					<button 
						class="btn side-by-side-btn" 
						on:click={changeText}
					>{buttontext[buttontextindex]}</button>
				</div>
			</div>
		</div>
	{:else if data.messages[0].type == '2'}
		<div class="grid flex-1 gap-2 lg:grid-cols-2">
			<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
				<div class="card">
					<h1 class="h1">Q{data.messages[0].id}: {data.messages[0].name}</h1>
					<p class="questiondesc">{data.messages[0].description}</p>
					<TruthTable truthTable={tb} {inputData} {outputData} />
				</div>
			</div>

			<div class="flex h-full flex-col gap-4 overflow-y-auto p-4">
				<div class="card">
					<h1 class="h1">Circuit:</h1>
					<Visualizer width={500} height={500} shdl={value} />
				</div>
			</div>
		</div>
		<button class="btn mt-4" on:click={changeText}>{buttontext[buttontextindex]}</button>
	{:else}{/if}
</main>
