<script lang="ts">
	import { le } from '@xata.io/client';
	import { onMount } from 'svelte';

	export let width: number = 500;
	export let height: number = 500;
	export let shdl: string = '';

	//visual
	let canvas: HTMLCanvasElement;
	let ctx: CanvasRenderingContext2D | null = null;

	//functional
	let inputs: string[];
	let outputs: string[];
	let wires: string[];
	let gates: string[];

	onMount(() => {
		ctx = canvas.getContext('2d');

		render();
	});

	function render() {
		//variables
		let trimmedString = parseText(shdl);
		inputs = parseInput(trimmedString);
		outputs = parseOutput(trimmedString);
		wires = parseWire(trimmedString);
		gates = parseGates(shdl);

		//positional
		let x = 200;
		let y = 200;
		let gate_width = 60;
		let gate_height = 40;
		let fontSize = 12;

		drawInputs(inputs);
		drawOutputs(outputs);

		let i = 1;
		gates.forEach((gate) => {
			let gateInfo = gate.split(' ');
			let gateName = gateInfo[0];
			let gateInputs;
			let gateOutputs;

			if (gateName === 'AND' || gateInfo[0] === 'OR' || gateInfo[0] === 'XOR') {
				gateInputs = gateInfo.slice(1, 3);
				gateOutputs = [gateInfo[3]];
				drawGate(gateName, x, y, gate_width, gate_height, fontSize, gateInputs, gateOutputs);
			} else if (gateName === 'NOT') {
				gateInputs = [gateInfo[1]];
				gateOutputs = [gateInfo[2]];
				drawGate(gateName, x, y, gate_width, gate_height, fontSize, gateInputs, gateOutputs);
			} else {
				//custom gate fuck fuck fuck
			}

			//inputs
			let length = inputs.length + 1;
			gateInputs.forEach((input) => {
				i = inputs.indexOf(input);
				if (i !== -1) {
					drawWire(x, y + (gate_height * (i + 1)) / length, 10, (height * (i + 1)) / length);
				} else {
					alert('FUUUUCCCCKCKKK');
				}
			});

			//outputs
			length = outputs.length + 1;
			i = 1;
			gateOutputs.forEach((output) => {
				i = outputs.indexOf(output);
				if (i !== -1) {
					drawWire(
						x + gate_width,
						y + (gate_height * (i + 1)) / length,
						width - 10,
						(height * (i + 1)) / length
					);
				} else {
					alert('FUUUUCCCCKCKKK');
				}
			});

			y = y + 100;
		});
	}

	//parser functions
	function parseInput(inputString: string) {
		// Regular expression to match INPUT lines
		const inputRegex = /INPUT\s+(\w+)/g;

		// Extracting all INPUT elements
		const inputs = [];
		let match;
		while ((match = inputRegex.exec(inputString)) !== null) {
			inputs.push(match[1]);
		}

		return inputs;
	}

	function parseOutput(inputString: string) {
		// Regular expression to match OUTPUT lines
		const outputRegex = /OUTPUT\s+(\w+)/g;

		// Extracting all OUTPUT elements
		const outputs = [];
		let match;
		while ((match = outputRegex.exec(inputString)) !== null) {
			outputs.push(match[1]);
		}

		return outputs;
	}

	function parseWire(inputString: string) {
		// Regular expression to match WIRE lines
		const wireRegex = /WIRE\s+(\w+)/g;

		// Extracting all WIRE elements
		const wires = [];
		let match;
		while ((match = wireRegex.exec(inputString)) !== null) {
			wires.push(match[1]);
		}

		return wires;
	}

	function parseGates(inputString: string) {
		// Regular expression to match STARTGATE and ENDGATE blocks along with their contents
		const gateRegex = /STARTGATE.*?ENDGATE/gms;

		// Extracting all occurrences of STARTGATE and ENDGATE blocks
		const gates = inputString.match(gateRegex) || [];

		// Removing the STARTGATE and ENDGATE blocks from the input string
		const trimmedString = inputString.replace(gateRegex, '');

		// Extracting individual lines from the trimmed string
		const lines = trimmedString
			.split('\n')
			.map((line) => line.trim())
			.filter((line) => line !== '');

		// Filter out lines starting with INPUT or OUTPUT
		const otherLines = lines.filter(
			(line) => !line.startsWith('INPUT') && !line.startsWith('OUTPUT')
		);

		// Combining other lines and gates
		const result = [...otherLines, ...gates];

		return result;
	}

	function parseText(inputString: string) {
		// Regular expression to match STARTGATE and ENDGATE blocks along with their contents
		const gateRegex = /STARTGATE.*?ENDGATE/gms;

		// Extracting all occurrences of STARTGATE and ENDGATE blocks
		const gates = inputString.match(gateRegex) || [];

		// Removing the STARTGATE and ENDGATE blocks from the input string
		const trimmedString = inputString.replace(gateRegex, '');

		// Extracting individual lines from the trimmed string
		const lines = trimmedString
			.split('\n')
			.map((line) => line.trim())
			.filter((line) => line !== '');

		// Combining lines and gates
		const result = [...lines].join('\n');
		// const result = [...gates].join('\n');

		return result;
	}

	// render functions
	function drawGate(
		name: string,
		x: number,
		y: number,
		width: number = 60,
		height: number = 40,
		fontSize: number = 12,
		inputs: string[],
		outputs: string[]
	) {
		if (ctx !== null) {
			//body
			ctx.beginPath();
			ctx.rect(x, y, width, height);
			ctx.stroke();

			//title
			ctx.font = fontSize + 'px Arial';
			const titleWidth = ctx.measureText(name).width;
			const marginX = (width - titleWidth) / 2;
			const marginY = (height + fontSize) / 2;
			ctx.fillText(name, x + marginX, y + marginY);

			//inputs
			let length = inputs.length + 1;
			let i = 1;
			inputs.forEach((input) => {
				ctx.beginPath();
				ctx.arc(x, y + (height * i) / length, 3, 0, 2 * Math.PI);
				ctx.stroke();
				i++;
			});

			//outputs
			length = outputs.length + 1;
			i = 1;
			outputs.forEach((output) => {
				ctx.beginPath();
				ctx.arc(x + width, y + (height * i) / length, 3, 0, 2 * Math.PI);
				ctx.stroke();
				i++;
			});
		}
	}

	function drawWire(x0: number, y0: number, x1: number, y1: number, name: string = '') {
		if (ctx !== null) {
			const width = x1 - x0;

			//text
			ctx.font = '14px Arial';
			ctx.fillText(name, x0 + width / 6 - 3, y0 - 3);

			//lines
			ctx.moveTo(x0, y0);
			ctx.lineTo(x0 + width / 3, y0);
			ctx.lineTo(x1 - width / 3, y1);
			ctx.lineTo(x1, y1);
			ctx.stroke();
		}
	}

	function drawInputs(inputs: string[]) {
		const length = inputs.length + 1;
		let i = 1;
		if (ctx !== null) {
			inputs.forEach((input) => {
				ctx.font = '14px Arial';
				ctx.fillText(input, 7, (height * i) / length - 10);

				ctx.beginPath();
				ctx.arc(10, (height * i) / length, 3, 0, 2 * Math.PI);
				ctx.stroke();
				i++;
			});
		}
	}

	function drawOutputs(outputs: string[]) {
		const length = outputs.length + 1;
		let i = 1;
		if (ctx !== null) {
			outputs.forEach((output) => {
				ctx.font = '14px Arial';
				ctx.fillText(output, width - 20, (height * i) / length - 7);

				ctx.beginPath();
				ctx.arc(width - 10, (height * i) / length, 3, 0, 2 * Math.PI);
				ctx.stroke();
				i++;
			});
		}
	}
</script>

<canvas {width} {height} bind:this={canvas} />

<style>
	canvas {
		background-color: transparent; /* Set the canvas background color to transparent */
		border: 1px solid black; /* Optional: Add a border for better visualization */
	}
</style>
