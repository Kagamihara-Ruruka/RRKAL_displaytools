# C3 先驗語意字典驗證器關卡 (C3 Prior Semantic Dictionary Validator Gate)

本文件定義未來 C3 先驗語意字典 YAML 檔案的驗證規則、設計原則與驗證器腳本的運作機制。本關卡旨在建立「裁判尺」，以確保未來填寫先驗語意字典時，所有條目與欄位均符合約定，嚴防運行時狀態或未授權的實作污染進入核心字典中。

## 驗證器腳本

驗證器位於產品庫路徑：
[validate_displaytools_c3_prior_semantic_dictionary.py](file:///L:/RRKAL_displaytools/scripts/validate_displaytools_c3_prior_semantic_dictionary.py)

### 執行方式

在產品庫根目錄下執行：
```bash
py -3 -B scripts/validate_displaytools_c3_prior_semantic_dictionary.py [YAML_FILE_PATH] [SCHEMA_FILE_PATH]
```
- `YAML_FILE_PATH`：選填。預設為 `docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml`。若檔案不存在，驗證器將正常結束並輸出 `not_applicable_dictionary_missing`，回傳值為 0。
- `SCHEMA_FILE_PATH`：選填。預設為 `docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json`。若 schema JSON 檔案損毀或遺失，驗證器將報錯並回傳值為 1。

## 核心驗證規則

### 1. JSON Schema v0 合規性
- 驗證器將載入 [c3_prior_semantic_dictionary.schema.v0.json](file:///L:/RRKAL_displaytools/docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json) 對 YAML 檔案的結構、類型進行強校驗。
- YAML 根節點必須為映射 (Mapping)，且必須包含 12 個 top-level sections，不得含有 schema 規定以外的欄位。

### 2. 禁用家族欄位 (Forbidden Field Families) 檢驗
- 驗證器將遞迴掃描 YAML 的所有鍵與值，禁止出現任何包含運行時、渲染器狀態、或未授權實作宣稱的屬性。
- 禁用欄位清單包括：`runtime_state`、`renderer_state`、`frame_buffer`、`framebuffer`、`callable`、`runtime_object`、`dataframe`、`raw_payload`、`raw_payload_contract`、`c1_direct_dependency`、`odoriba_bypass`、`ui_state_as_truth`、`legacy_runtime_patch_as_ideal_form`、`implementation_authorized`、`readiness_claimed`。

### 3. 高風險裸詞 Rejection
- 在 `prior_terms` 中，所有先驗詞彙的 `term_id` 均不得直接使用以下裸詞 (bare terms)：`layer`、`mask`、`view`、`projection`、`frame`、`render`、`recipe`。此舉是為了避免將特定近似功能或實作細節直接升格為核心先驗詞彙。

### 4. 特殊業務合約校驗
- **配方唯一真理**：在 `recipe_authoring` 中，`recipe_owns_truth` 與 `ui_does_not_own_truth` 必須全為 `True`。
- **C4 中介調停**：在 `c4_mediation` 中，`ingress_mediated_by_c4`、`egress_mediated_by_c4`、`direct_c3_to_c1_forbidden` 必須全為 `True`。
- **未解 stop_lines 約束**：所有 `stop_lines` 的 `blocked_claims` 均不得含有 `implementation_authorized`，且 `unknown_stop_lines` 的每一個 entry 均必須指定 `resolution_gate` 作為後續的解鎖條件。