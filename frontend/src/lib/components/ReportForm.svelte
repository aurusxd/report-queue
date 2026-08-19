<script lang="ts">
    let {
        email = $bindable(),
        reportType = $bindable(),
        handleSubmit,
        isSubmitted,
    }: {
        email: string;
        reportType: string;
        handleSubmit: () => void;
        isSubmitted: boolean;
    } = $props();
</script>

<label class="block text-stale-300 text-sm font-medium mb-1.5 text-white"
    >Email:</label
>
<div class="space-y-5">
    <input
        type="email"
        bind:value={email}
        placeholder="your@email.com"
        class="
            w-full px-4 py-2.5 bg-slate-900/50 border border-slate-600
            rounded-xl text-white placeholder:text-slate-500
            focus:border-orange-500 focus:ring-2 focus:ring-orange-500/30
            focus:outline-none transition
            "
    />
</div>
<div>
    <label
        class="block text-stale-300 text-sm font-medium mb-1.5 text-white mt-5"
    >
        Тип отчёта
    </label>

    <select
        bind:value={reportType}
        class="w-full px-4 py-2.5 bg-slate-900/50 border border-slate-600
                           rounded-xl text-white
                           focus:border-orange-500 focus:ring-2 focus:ring-orange-500/30
                           focus:outline-none transition"
    >
        <option value="Sales">📊 Продажи</option>
        <option value="Inventory">📦 Остатки</option>
        <option value="Customers">👥 Клиенты</option>
    </select>
</div>

<button
    onclick={handleSubmit}
    disabled={!email.trim() || isSubmitted}
    class="w-full py-3 bg-gradient-to-r from-orange-100 to-orange-600
                       text-white font-medium rounded-xl
                       hover:from-orange-100 hover:to-orange-700
                       active:scale-[0.98]
                       disabled:opacity-50 disabled:active:scale-100
                       transition-all duration-200 mt-5"
>
    {#if isSubmitted}
        ⏳ Генерация...
    {:else}
        ✨ Сгенерировать
    {/if}
</button>
