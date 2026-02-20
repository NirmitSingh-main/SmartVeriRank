`timescale 1ns/1ps

module tb_fifo;

logic clk = 0;
always #5 clk = ~clk;

logic rst;
logic wr_en, rd_en;
logic [7:0] din;
logic [7:0] dout;
logic full, empty;

fifo uut (
    .clk(clk),
    .rst(rst),
    .wr_en(wr_en),
    .rd_en(rd_en),
    .din(din),
    .dout(dout),
    .full(full),
    .empty(empty)
);

initial begin
    rst = 1;
    wr_en = 0;
    rd_en = 0;
    din = 0;
    #20 rst = 0;

    repeat(100) begin
        @(posedge clk);
        wr_en = $urandom_range(0,1);
        rd_en = $urandom_range(0,1);
        din = $urandom;
    end

    #100 $finish;
end

endmodule

