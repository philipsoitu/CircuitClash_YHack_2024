<script>
  // @ts-ignore
  import { SignIn, SignOut } from "@auth/sveltekit/components"
  import { page } from "$app/stores"
</script>

<h1>SvelteKit Auth Example</h1>
<div>
  {#if $page.data.session}
    {#if $page.data.session.user?.image}
      <img
        src={$page.data.session.user.image}
        class="avatar"
        alt="User Avatar"
      />
    {/if}
    <span class="signedInText">
      <small>Signed in as</small><br />
      <strong>{$page.data.session.user?.name ?? "User"}</strong>
    </span>
   
  {:else}
    <span class="notSignedInText">You are not signed in</span>
    <SignIn>
      <div slot="submitButton" class="buttonPrimary">Sign in</div>
    </SignIn>
  {/if}

   <SignOut>
      <div slot="submitButton" class="btn">Sign out</div>
    </SignOut>
</div>
