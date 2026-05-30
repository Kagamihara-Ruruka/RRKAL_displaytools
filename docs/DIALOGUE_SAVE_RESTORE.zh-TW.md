# dialogue-save 對話還原流程

最後更新：2026-05-30

## 目的

這份文件說明如何從私有 repo `Kagamihara-Ruruka/dialogue-save` 還原目前 RRKAL_displaytools Codex 對話的原始 rollout JSONL。

公開 `RRKAL_displaytools` repo 不保存 raw transcript；这里只保存還原流程。

## 私有 repo 位置

```text
https://github.com/Kagamihara-Ruruka/dialogue-save
```

目前 session folder：

```text
RRKAL_displaytools/rrkal-displaytools-cloud-transition__2026-05-30__019e6e98/
```

## 內容結構

```text
README.md
metadata.json
artifacts-manifest.json
transcript.raw.jsonl.gz.part001
transcript.raw.jsonl.gz.part002
transcript.raw.jsonl.gz.part003
```

`metadata.json` 記錄：

- thread id: `019e6e98-1e83-76c2-93f9-a29969f19169`
- source rollout path
- copied rollout byte size
- copied rollout SHA-256
- transcript storage mode
- private repo requirement

## 還原步驟

在任一乾淨暫存位置執行，不要放進 `L:\RRKAL_displaytools`。

```powershell
$work = Join-Path $env:TEMP "dialogue-save-restore"
Remove-Item -LiteralPath $work -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force -Path $work | Out-Null
Set-Location $work

git clone https://github.com/Kagamihara-Ruruka/dialogue-save.git
Set-Location dialogue-save\RRKAL_displaytools\rrkal-displaytools-cloud-transition__2026-05-30__019e6e98

Get-Content -Encoding Byte -Path transcript.raw.jsonl.gz.part001, transcript.raw.jsonl.gz.part002, transcript.raw.jsonl.gz.part003 |
  Set-Content -Encoding Byte -Path transcript.raw.jsonl.gz

gzip -d transcript.raw.jsonl.gz
Get-FileHash -Algorithm SHA256 transcript.raw.jsonl
```

若 Windows 環境沒有 `gzip`，可用 PowerShell/.NET 解壓：

```powershell
$gz = [System.IO.File]::OpenRead("transcript.raw.jsonl.gz")
$out = [System.IO.File]::Create("transcript.raw.jsonl")
$stream = [System.IO.Compression.GzipStream]::new($gz, [System.IO.Compression.CompressionMode]::Decompress)
try {
    $stream.CopyTo($out)
} finally {
    $stream.Dispose()
    $out.Dispose()
    $gz.Dispose()
}
```

## 驗證

還原後的 `transcript.raw.jsonl` SHA-256 應與 `metadata.json` 的 `copied_rollout_sha256` 相同。

## 使用規則

- 只在 handoff 文件不足以接續時讀 raw transcript。
- 不要把 raw transcript 複製到公開 repo。
- 不要把 `dialogue-save` clone 留在 `L:`。
- 使用完後清除暫存目錄。
- 若要引用到公開 repo，只能摘要成 handoff / decisions / development log。

## 另一位 agent 的最短指令

```text
先讀 RRKAL_displaytools/docs/CODEX_CLOUD_HANDOFF.zh-TW.md。
若仍需要完整對話，再從 private repo dialogue-save 還原 RRKAL_displaytools/rrkal-displaytools-cloud-transition__2026-05-30__019e6e98 的 transcript.raw.jsonl。
還原後只抽取接力所需決策，不要把 raw transcript 放進公開 repo。
```