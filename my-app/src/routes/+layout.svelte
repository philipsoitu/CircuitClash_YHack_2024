<script lang="ts">
	import '../main.css';
	export let data;
	

</script>

<svelte:head>
    <title>Info Toit</title>
</svelte:head>

<div
    class="flex justify-between rounded-2xl border-2 main px-4 py-2"
>
    <a class="flex items-center gap-2" href="/">
        <h1 class="h1">Circuit</h1>
    </a>

    <div class="flex items-center gap-4">
        <a class="btn bg-yellow-950 btn-sm" href="/circuit"> Levels </a>

        <a class="btn btn-sm" href="/docs"> Docs </a>

        {#if !data.user}
            <div class="btn btn-sm">Sign In</div>
        {:else}
            <button class="btn btn-flat h-10 w-10 p-0">
                <img src={data.avatar} class="object-cover" alt="your user avatar" />
            </button>
        {/if}
    </div>
</div>


<slot />
