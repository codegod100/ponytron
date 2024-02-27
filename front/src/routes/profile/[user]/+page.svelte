<script>
  export let data;
  import { subscribe, unsubscribe } from "$lib/common.js";
  import { invalidateAll } from "$app/navigation";
</script>

<div>Id: {data.user.id}</div>
<div>Username: {data.user.username}</div>
<div>
  Status:
  {#if data.friends && data.friends.includes(data.user.username)}
    following <button
      on:click={async () => {
        await unsubscribe({ user: data.user.username, my_info: data.username });
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
