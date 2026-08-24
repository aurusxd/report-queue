<script lang="ts">
    import { onMount } from "svelte";
    import type { Report } from "$lib/types/report";
    import ReportItem from "$lib/components/ReportItem.svelte";
    import ReportForm from "$lib/components/ReportForm.svelte";
    import type { ReportRespone } from "$lib/types/report";

    let email = $state("");
    let reportType = $state("Sales");
    let count = 1;
    let isSubmitted = $state(false);
    let loading = $state(true);
    let error = $state<string | null>(null);
    let reports = $state<Report[]>([]);
    let processingReport = $state(0);
    let totalReport = $state(0);
    let completedReport = $state(0);

    async function getReports() {
        const response = await fetch(`http://127.0.0.1:8000/reports`);
        return await response.json();
    }

    async function handleSubmit() {
        if (!email.trim()) return;
        const data: ReportRespone = {
            email: email,
            status: "queued",
            type: "Customers",
        };
        await generateReport(data);
        console.log("prviet");
        isSubmitted = false;
    }

    async function handleStatus(reportId: number) {
        const response = await fetch(
            `http://127.0.0.1:8000/reports/${reportId}`,
        );
        if (!response) return;
        const report = await response.json();

        switch (report.status) {
            case "queued":
                report.status = "processing";
                break;
            case "processing":
                report.status = "completed";
                break;
        }
    }

    async function generateReport(data: ReportRespone) {
        isSubmitted = true;
        const response = await fetch(`http://127.0.0.1:8000/reports/create`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        if (!response) return;

        await new Promise((resolve) => {
            setTimeout(resolve, 3000);
        });
    }

    onMount(async () => {
        try {
            reports = await getReports();
        } catch (err) {
            error = err instanceof Error ? err.message : "Unknown error";
        } finally {
            loading = false;
        }
    });
</script>

<section>
    <h1 class="font-bold text-white text-4xl text-center pt-5">
        Добро пожаловать
    </h1>
    <div
        class="w-full max-w-md bg-slate-800/50 backdrop-blur-xl rounded-2xl p-8 shadow-2xl border border-slate-700 mt-5"
    >
        <ReportForm bind:email bind:reportType {handleSubmit} {isSubmitted} />

        <div class="text-center pt-10">
            <label class=" text-white font-bold text-sm">
                Недавние отчёты:
            </label>
            <div class="flex items-center gap-3">
                <p class="text-sm text-white">Всего: {totalReport}</p>
                <p class="text-sm text-white">
                    В процессе: {processingReport == undefined
                        ? 0
                        : processingReport}
                </p>
                <p class="text-sm text-white">
                    Завершенные: {completedReport == undefined
                        ? 0
                        : completedReport}
                </p>
            </div>

            {#each reports as report}
                <ReportItem {report} {handleStatus} />
            {/each}
        </div>
    </div>
</section>
