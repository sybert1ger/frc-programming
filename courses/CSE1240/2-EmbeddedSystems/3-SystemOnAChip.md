---
title: System on a Chip (FPGA & ASIC)
layout: coursepage
---

A system on a chip is an integrated circuit that integrates all components of a computer into a single chip. In effect, modern SoC don't actually follow this definition precisely. Most of the time, it is more of a declaration of *purpose* instead of *implementation*.

Typically, the direction of a SoC is:

- Small and lightweight
- Purpose-specific
- Integrated components for peripherals
- Self-regulating and sustaining

Generally, you can think of a SoC as a purpose-built processor with internal regulators and components that make integration into a system easy.

### FPGA
A Field-Programmable Gate Array is a way to fabricate SoC that is designed to be configured after manufacturing.

FPGAs contain programmable logic components called "logic blocks", and a hierarchy of reconfigurable interconnects that allow the blocks to be "wired together" – somewhat like many (changeable) logic gates that can be inter-wired in (many) different configurations. Logic blocks can be configured to perform complex combinational functions, or merely simple logic gates like AND and XOR. In most FPGAs, the logic blocks also include memory elements, which may be simple flip-flops or more complete blocks of memory.

Technically speaking, FPGAs are not constrained in any programming perspective. They can solve any computable problem. Their advantage lies in the capacity to be efficient - their parallel nature and deep programming allow for very fast computation in certain cases. Their disadvantage lies in the fact that it is very difficult get high clock speeds and manufacture smaller parts. They don't lend themselves to getting faster like other microprocessors do.

### ASIC
An Application Specific Integrated Circuit is similar to an FPGA, but without the capacity to be changed. They are designed and built with a purpose in mind, and can only accomplish that purpose.

In the modern economy, ASICs are becoming less popular. In the past, they were made because of higher performance capabilities and lower costs per unit. But FPGA has become an affordable technology - so much so that companies opt to buy FPGAs instead of ASIC even without the need to reprogram it. (economies of scale bring FPGA prices down)
