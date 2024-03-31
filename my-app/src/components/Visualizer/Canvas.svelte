<script lang="ts">
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

	//gate positioning
	let layerInputs: string[][];
	let layers: string[][];

	onMount(() => {
		ctx = canvas.getContext('2d');
		render();
	});

	function render() {
		let trimmedString = parseText(shdl);
		inputs = parseInput(trimmedString);
		outputs = parseOutput(trimmedString);
		wires = parseWire(trimmedString);
		gates = parseGates(shdl);

		layerInitializer();

		let x: number;
		let y: number;
		let gate_width = 60;
		let gate_height = 40;
		let fontSize = 12;

		for (let i = 0; i < layers.length; i++) {
			let layer = layers[i];

			for (let j = 0; j < layer.length; j++) {
				x = (width * (i + 1)) / (layers.length + 1);
				y = (height * (j + 1)) / (layer.length + 1);

				let gateInfo = layer[j].split(' ');
				let gateName = gateInfo[0];
				let gateInputs: string[];
				let gateOutputs: string[];
				if (gateName === 'AND' || gateInfo[0] === 'OR' || gateInfo[0] === 'XOR') {
					gateInputs = gateInfo.slice(1, 3);
					gateOutputs = [gateInfo[3]];
					drawGate(gateName, x, y, gate_width, gate_height, fontSize, gateInputs, gateOutputs);
				} else if (gateName === 'NOT') {
					gateInputs = [gateInfo[1]];
					gateOutputs = [gateInfo[2]];
					drawGate(gateName, x, y, gate_width, gate_height, fontSize, gateInputs, gateOutputs);
				} else {
					gateInputs = [];
					gateOutputs = [];
					//custom gate
				}

				for (let input = 0; input < gateInputs.length; input++) {
					let layer_index: number;
					for (layer_index = 0; layer_index < layerInputs.length; layer_index++) {
						if (layerInputs[layer_index].includes(gateInputs[input])) {
							break;
						}
					}

					let initX: number = x;
					let initY: number = y + (gate_height * (input + 1)) / (gateInputs.length + 1);
					let targetX: number = initX - width / (layers.length + 1) + gate_width;
					let targetY: number =
						(height * (layerInputs[layer_index].indexOf(gateInputs[input]) + 1)) /
							(layerInputs[layer_index].length + 1) +
						(layer_index >= 1 ? gate_height / 2 : 0);
					drawWire(initX, initY, targetX, targetY);
				}

				for (let output = 0; output < gateOutputs.length; output++) {
					if (outputs.includes(gateOutputs[output])) {
						console.log(gateName, i, j);
						let initX: number = x + gate_width;
						let initY: number = y + (gate_height * (output + 1)) / (gateOutputs.length + 1);
						let targetX: number = width - 10;
						let targetY: number = height * (outputs.indexOf(gateOutputs[output]) + 1)/ (outputs.length + 1);
						drawWire(initX, initY, targetX, targetY);
					}
				}
			}
		}

		drawInputs(inputs);
		drawOutputs(outputs);
	}

	function layerInitializer() {
		// Parse SHDL and extract necessary information
		let trimmedString = parseText(shdl);
		inputs = parseInput(trimmedString);
		outputs = parseOutput(trimmedString);
		wires = parseWire(trimmedString);
		gates = parseGates(shdl);

		// Initialize layers
		layerInputs = [inputs];
		layers = [];

		let info;
		let gateName;
		let gateInputs: string[];
		let gateOutputs: string[];

		gates.forEach((gate) => {
			info = gate.split(' ');
			gateName = info[0];

			switch (gateName) {
				case 'AND':
				case 'OR':
				case 'XOR':
					gateInputs = info.slice(1, 3);
					gateOutputs = [info[3]];
					break;
				case 'NOT':
					gateInputs = [info[1]];
					gateOutputs = [info[2]];
					break;
				default:
					// Custom gate
					// Handle custom gates as per your requirement
					return;
			}

			// Find the layer where all inputs are available
			let targetLayer = -1;
			for (let i = 0; i < layerInputs.length; i++) {
				if (isSubset(gateInputs, layerInputs[i])) {
					targetLayer = i;
					break;
				}
			}

			if (targetLayer !== -1) {
				if (layerInputs.length <= targetLayer + 1) {
					layerInputs.push([]);
				}
				layerInputs[targetLayer + 1].push(...gateOutputs);
			} else {
				// Inputs not found in any layer, place gate in a new layer
				layerInputs.push([...gateInputs, ...gateOutputs]);
			}
		});

		gates.forEach((gate) => {
			info = gate.split(' ');
			gateName = info[0];

			switch (gateName) {
				case 'AND':
				case 'OR':
				case 'XOR':
					gateInputs = info.slice(1, 3);
					gateOutputs = [info[3]];
					break;
				case 'NOT':
					gateInputs = [info[1]];
					gateOutputs = [info[2]];
					break;
				default:
					// Custom gate
					// Handle custom gates as per your requirement
					return;
			}

			let i = 0;
			let remaining: string[] = gateInputs;
			let gateAlreadyAdded = false; // Flag to check if gate is already added
			layerInputs.forEach((layerInput) => {
				remaining = remaining.filter((item) => !layerInput.includes(item));
				if (remaining.length === 0 && !gateAlreadyAdded) {
					if (!layers[i] || !layers[i].includes(gate)) {
						// Check if the gate is not already added
						layers[i] = [...(layers[i] || []), gate];
						gateAlreadyAdded = true; // Set flag to true
					}
				}
				i++;
			});
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
			(line) => !line.startsWith('INPUT') && !line.startsWith('OUTPUT') && !line.startsWith('WIRE')
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

	function isSubset(subset: any[], superset: any[]) {
		return subset.every((element) => superset.includes(element));
	}
</script>

<canvas {width} {height} bind:this={canvas} />

<style>
	canvas {
		background-color: transparent; /* Set the canvas background color to transparent */
		border: 1px solid black; /* Optional: Add a border for better visualization */
	}
</style>
