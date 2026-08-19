export interface Report {
    id: number;
    type: string;
    email: string;
    status: "queued" | "processing" | "completed";
}