# Resource Isolation Boundaries for Parallel Agent Execution

**Status: PUBLIC-SAFE PROTOCOL DOCUMENT — OS/TOOL NEUTRAL**

Issue: hummbl-dev/hummbl-dev#133
Parent: hummbl-dev/hummbl-dev#125

## Purpose

Document resource isolation boundaries for parallel agent execution, especially when agents run stress tests, integration tests, build loops, fuzzing, or large-scale generated-code workflows.

This is a public-safe protocol document, not a machine-specific runbook.

## Risk categories

| Category | Risk | Failure mode |
|----------|------|-------------|
| CPU | Starvation of other processes | Runaway build/test loops consume all cores |
| Memory | OOM kills, swap thrashing | Large test suites or fuzzing exhaust available RAM |
| PID/process count | Fork bombs, process table exhaustion | Unbounded child processes spawn |
| Disk space | Disk full, write failures | Temp files, build artifacts, or logs fill disk |
| Disk I/O | I/O contention, slow builds | Parallel agents compete for disk throughput |
| Network/socket exhaustion | Port conflicts, connection limits | Agents bind same ports or exhaust file descriptors |
| Temp files | Orphaned files, disk growth | Agents crash without cleanup |
| Cache growth | Cache invalidation storms, disk bloat | Build caches grow unbounded |
| Runaway child processes | Zombie processes, resource leak | Child processes outlive parent agent |

## Preflight checks

Before running heavy workflows (stress tests, integration tests, build loops, fuzzing, large-scale code generation):

- [ ] **CPU**: Check available CPU headroom (agent should not consume >80% of available cores for >5 minutes without operator approval)
- [ ] **Memory**: Check available memory (agent should not consume >75% of available RAM)
- [ ] **Disk space**: Check available disk space (agent should leave >10% free)
- [ ] **Disk I/O**: Check if other heavy I/O operations are running
- [ ] **Network**: Check if required ports are available; verify no port conflicts
- [ ] **Process count**: Check current process count; verify headroom for expected child processes
- [ ] **Temp directory**: Verify temp directory exists and has space; plan cleanup path
- [ ] **Cache**: Check cache size; plan eviction if near limits
- [ ] **Concurrency**: Verify how many parallel agents/workflows are already running

## Limits and boundaries

### Generic limits (apply everywhere)

- **Max CPU per agent**: 80% of available cores for >5 minutes requires operator approval
- **Max memory per agent**: 75% of available RAM
- **Max disk usage per agent**: Leave >10% free disk space
- **Max temp file age**: Clean up temp files older than 1 hour
- **Max child process count per agent**: 50 concurrent child processes
- **Max network connections per agent**: 100 concurrent connections
- **Max workflow duration without checkpoint**: 30 minutes (checkpoint or report progress)

### Container/cgroup boundaries (examples only)

When containers or cgroups are available:
- Set CPU shares/limits per container
- Set memory limits per container
- Set PID limits per container
- Set disk I/O limits per container
- Use read-only root filesystem where possible
- Mount tmpfs for temp directories with size limits

### CI boundaries (examples only)

In CI environments:
- Use job-level resource limits
- Set job timeouts
- Use isolated runners/workers per job
- Clean up workspace after job completion
- Limit concurrent jobs per repo

### Local developer-machine boundaries

On local developer machines:
- Run heavy workflows in isolated worktrees
- Use `nice`/`taskset` or equivalent to reduce priority
- Monitor resource usage during long workflows
- Clean up after workflow completion
- Do not run multiple heavy workflows simultaneously without operator approval

## Abort conditions

Abort immediately and report if:
- Available memory drops below 10% of total
- Available disk space drops below 5% of total
- Process count exceeds 90% of system limit
- A child process is unresponsive for >60 seconds
- Network port conflict is detected
- Operator sends cancellation signal

Abort with cleanup if:
- Workflow exceeds approved time limit
- Resource usage exceeds approved budget
- Test suite begins failing due to resource contention (not code changes)

## Cleanup expectations

After workflow completion or abort:
- Remove all temp files created by the workflow
- Kill all child processes spawned by the workflow
- Release all network ports bound by the workflow
- Clear build artifacts if not needed for downstream work
- Report resource usage summary (CPU time, memory peak, disk used, duration)

## Receipt requirements for heavy commands

For any command that runs >5 minutes or consumes significant resources:

- Command executed
- Duration
- CPU time consumed
- Peak memory usage
- Disk space consumed
- Number of child processes spawned
- Exit status
- Cleanup actions taken
- Resource usage summary

## Human/operator gates

Operator approval required before:
- Running workflows expected to take >30 minutes
- Consuming >50% of available CPU for >10 minutes
- Consuming >50% of available RAM
- Writing >1GB of temp files
- Spawning >20 concurrent child processes
- Running destructive cleanup (deleting directories, killing processes)
- Running fuzzing or stress tests that may generate large outputs
- Running workflows that bind to well-known ports

## Test integrity requirement

**Tests must not be weakened merely to fit resource limits.**

If a test suite cannot complete within resource boundaries:
1. Report the resource constraint as a blocker
2. Do not delete, skip, or downscope tests to fit
3. Request operator approval for expanded resources
4. Or: split the test suite into smaller batches with checkpointing

## Local vs CI guidance

| Concern | Local developer machine | CI environment |
|---------|------------------------|----------------|
| Resource limits | Advisory; operator monitors | Enforced by job config |
| Concurrency | Operator-controlled | Job/runner isolated |
| Cleanup | Agent responsibility | Workspace cleanup automatic |
| Timeout | Advisory; operator decides | Enforced by job timeout |
| Approval | Inline operator approval | Pre-configured in pipeline |

## Related documents

- Agent Mutation Guardrails: `AGENT_MUTATION_GUARDRAILS.md` (hummbl-dev/hummbl-dev#131)
- Migration Contract Template: `MIGRATION_CONTRACT_TEMPLATE.md`
- Failure queue and process-patch log: hummbl-dev/hummbl-dev#132

## Non-goals

- No new production scheduler
- No OS-specific implementation required
- No promises about available local infrastructure
- No private hostnames, machine names, paths, secrets, or local capacity claims
