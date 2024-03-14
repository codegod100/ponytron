<script>
  export let data;
  import {
    create_status,
    subscribe,
    unsubscribe,
    status_to_link,
  } from "$lib/common.js";
  import { invalidateAll } from "$app/navigation";
  let body = "";
</script>

<div>Id: {data.user.id}</div>
<div>Username: {data.user.username}</div>
{#if data.username != data.user.username}
  <div>
    Status:
    {#if data.friends && data.friends.includes(data.user.username)}
      following <button
        on:click={async () => {
          await unsubscribe({
            user: data.user.username,
            my_info: data.username,
          });
          invalidateAll();
        }}
        class="btn variant-filled">unfollow</button
      >
    {:else}
      not following <button
        on:click={async () => {
          await subscribe({ user: data.user.username, my_info: data.username });
          invalidateAll();
        }}
        class="btn variant-filled">follow</button
      >
    {/if}
  </div>
{/if}
<div>
  Statuses:
  {#each data.statuses as status}
    <div class="p-2">
      <div>{status.record.text}</div>
      <div class="text-xs">
        <a href={status_to_link(status)}>{new Date(status.record.created_at)}</a
        >
      </div>
    </div>
  {/each}
</div>

<div>
  {#if data.user.username == data.username}
    <div>Enter status update</div>
    <textarea bind:value={body} class="input"></textarea>
    <button
      on:click={async () => {
        await create_status({ jwt: data.jwt, body });
        invalidateAll();
        body = "";
      }}
      class="btn variant-filled">Submit</button
    >
  {/if}
</div>
