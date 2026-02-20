module fifo #(parameter DEPTH = 4, WIDTH = 8)(
    input  logic clk,
    input  logic rst,
    input  logic wr_en,
    input  logic rd_en,
    input  logic [WIDTH-1:0] din,
    output logic [WIDTH-1:0] dout,
    output logic full,
    output logic empty
);

logic [WIDTH-1:0] mem [DEPTH-1:0];
logic [2:0] wr_ptr, rd_ptr, count;

assign full  = (count == DEPTH);
assign empty = (count == 0);

// Basic FIFO logic
always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
        wr_ptr <= 0;
        rd_ptr <= 0;
        count  <= 0;
    end else begin

        // Overflow
        if (wr_en && full) begin
            $error("ERROR: [FIFO_OVERFLOW] Module=fifo Time=%0t Write when full", $time);
        end

        // Underflow
        if (rd_en && empty) begin
            $warning("WARNING: [FIFO_UNDERFLOW] Module=fifo Time=%0t Read when empty", $time);
        end

        // Write operation
        if (wr_en && !full) begin
            mem[wr_ptr] <= din;
            wr_ptr <= wr_ptr + 1;
            count <= count + 1;
        end

        // Read operation
        if (rd_en && !empty) begin
            dout <= mem[rd_ptr];
            rd_ptr <= rd_ptr + 1;
            count <= count - 1;
        end

        // POINTER MISMATCH (artificial verification failure)
        if (wr_ptr > DEPTH || rd_ptr > DEPTH) begin
            $error("ERROR: [POINTER_MISMATCH] Module=fifo Time=%0t Pointer out of range", $time);
        end

        // DATA CORRUPTION check (simulate corruption randomly)
        if (count > 0 && mem[0] === 8'hXX) begin
            $error("ERROR: [DATA_CORRUPTION] Module=fifo Time=%0t Unknown data detected", $time);
        end

        // INVALID STATE (count inconsistent)
        if (count > DEPTH) begin
            $error("ERROR: [INVALID_STATE] Module=fifo Time=%0t Count exceeded DEPTH", $time);
        end

    end
end

endmodule
