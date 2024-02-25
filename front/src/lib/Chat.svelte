<script>
  let message = "";
  import { get_chat, submit_chat, storedname } from "$lib/common";
  import { page } from "$app/stores";
  import { invalidateAll } from "$app/navigation";
</script>

{#await get_chat($page.params.name) then chat}
  {#each chat.messages as message}
    <div>
      {message.author}: {message.body}
    </div>
  {/each}
{/await}

<form
  on:submit|preventDefault={async () => {
    await submit_chat({
      chat_name: $page.params.name,
      user: $storedname,
      body: message,
    });
    message = "";
    invalidateAll();
  }}
>
  <input type="text" bind:value={message} />
</form>
