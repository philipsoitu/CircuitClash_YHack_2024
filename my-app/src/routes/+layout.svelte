<script lang="ts">
	import '../main.css';
	export let data;
	

</script>

<svelte:head>
    <title>Info Toit</title>
</svelte:head>

<div
    class="sticky inset-2 z-50 m-2 flex justify-between rounded-lg border-2 border-dark bg-white px-4 py-2"
>
    <a class="flex items-center gap-2" href="/">
        <h1 class="h1">Circuit</h1>
    </a>

    <div class="flex items-center gap-4">
        <a class="btn btn-sm" href="/commerce"> Commerce </a>

        <a class="btn btn-sm" href="/"> Chercher une maison </a>

        <a class="btn btn-sm" href="/messages"> Messages citoyens </a>

        {#if !data.user}
            <a class="btn btn-sm" href="/sign-in">Sign In</a>
        {:else}
            <button class="btn btn-flat h-10 w-10 p-0">
                <img src={data.avatar} class="object-cover" alt="your user avatar" />
            </button>
        {/if}
    </div>
</div>


<slot />
