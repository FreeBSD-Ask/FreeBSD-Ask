# BSD 许可证概览

BSD 许可证是自由软件许可证谱系中的重要类别，以其宽松的使用条款为显著特征，在现代开源软件生态系统中占据核心地位。BSD 许可证代表了一种平衡开源精神与商业需求的制度设计。本文仅列出主要的、受 OSI（开放源代码促进会）认可的 BSD 许可证（不包括 BSD-4-Clause）。更多 BSD 许可证信息参见 OSI Approved Licenses[EB/OL]. [2026-03-25]. <https://opensource.org/licenses?ls=BSD>，以及 SPDX License List[EB/OL]. [2026-03-25]. <https://spdx.org/licenses/>. SPDX 提供标准化的许可证标识列表。

下文列出的所有 BSD 许可证均属于非 copyleft（著佐权）许可证范畴，即不强制要求修改后的衍生版本仍必须作为自由软件发布，这一特性使得它们在商业与开源技术融合的应用场景中具有一定优势。更多关于 BSD 许可证与 copyleft 范式比较的讨论参见 BSD 许可证的问题[EB/OL]. [2026-03-25]. <https://www.gnu.org/licenses/bsd.zh-cn.html>.

BSD 许可证条款编号用于表征附加义务和限制条件的复杂度。0BSD 限制最少，4BSD 限制最多。

## BSD 零条款许可证（Zero-Clause BSD，0BSD）

BSD 零条款许可证是 BSD 许可证系列中限制最少的一种，尽管其名称包含“BSD”，但它并非来自传统的 BSD 家族。

此许可证是 ISC 许可证的变体。ISC 许可证源自 Internet Systems Consortium，是一种简洁的宽松许可证。0BSD 是一种类似公共领域的宽松许可证。

```text
Zero-Clause BSD
=============

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE
FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY
DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

---

BSD 零条款许可证

特此授予任何人出于任何目的使用、复制、修改和/或分发本软件的权限，无论是否收取费用。

本软件按“原样”提供，作者不对本软件作出任何保证，包括所有对适销性和适用性的暗示保证。在任何情况下，作者均不对因使用、数据或利润的损失所造成的任何特殊、直接、间接或后果性损害，或任何形式的损害承担责任，无论该损害是在合同诉讼、过失或其他侵权行为中引起，或由使用或执行本软件所引起。

## BSD 一条款许可证（The 1-Clause BSD License，BSD-1-Clause）

BSD 一条款许可证在零条款的基础上增加了版权声明的要求。

```text
Copyright (c) [年份]
[组织名称] [All rights reserved].

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
THIS SOFTWARE IS PROVIDED BY [Name of Organization] "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL [Name of Organization] BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

版权所有 (c) [年份]

[组织名称] 保留所有权利。

在满足以下条件的前提下，允许在源代码和二进制形式中重新分发和使用本软件，无论是否经过修改：

源代码的再发布必须保留上述版权声明、本条件列表以及以下免责声明。
本软件由 [组织名称] 按“原样”提供，不作任何明示或暗示的保证，包括但不限于对适销性和特定用途适用性的暗示保证。在任何情况下，[组织名称] 均不对因使用本软件而引起的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用、数据或利润的损失，或业务中断）承担责任，无论责任主张基于合同、严格责任或侵权行为（包括过失或其他），即使已被告知可能发生此类损害。

## BSD 两条款许可证（The 2-Clause BSD License，BSD-2-Clause）

BSD 两条款许可证是使用较为广泛的一种 BSD 许可证。BSD 两条款许可证即 FreeBSD 许可证，亦称为简化版 BSD 许可证，是 FreeBSD 项目优先选用的许可证。该许可证删除了原始 BSD 许可证（即 BSD-4-Clause）中的广告条款，仅要求保留版权声明。广告条款要求在宣传材料中提及原作者，该条款因实际使用不便而被移除。

```text
Copyright <年份> <版权持有者>

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

版权所有 <年份> <版权持有者>

在满足以下条件的前提下，允许在源代码和二进制形式中重新分发和使用本软件，无论是否经过修改：

1. 源代码的再发布必须保留上述版权声明、本条件列表以及以下免责声明。

2. 二进制形式的再发布必须在随附的文档和/或其他材料中复制上述版权声明、本条件列表以及以下免责声明。

本软件由版权持有者和贡献者按“原样”提供，不作任何明示或暗示的保证，包括但不限于对适销性和特定用途适用性的暗示保证。在任何情况下，版权持有者或贡献者均不对因使用本软件而引起的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用、数据或利润的损失，或业务中断）承担责任，无论责任主张基于合同、严格责任或侵权行为（包括过失或其他），即使已被告知可能发生此类损害。

## BSD 三条款许可证（The 3-Clause BSD License，BSD-3-Clause）

BSD 三条款许可证在两条款的基础上增加了对使用作者名义推广的限制。BSD 三条款许可证亦称为新 BSD 许可证或修改版 BSD 许可证。此许可证删除了原始 BSD 许可证（即 BSD-4-Clause）中的广告条款，并额外限制以作者名义推广衍生产品。

```text
Copyright <年份> <版权持有者>

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

版权所有 <年份> <版权持有者>

在满足以下条件的前提下，允许在源代码和二进制形式中重新分发和使用本软件，无论是否经过修改：

1. 源代码的再发布必须保留上述版权声明、本条件列表以及以下免责声明。

2. 二进制形式的再发布必须在随附的文档和/或其他材料中复制上述版权声明、本条件列表以及以下免责声明。

3. 未经事先书面许可，不得使用版权持有者或其贡献者的姓名为源自本软件的产品背书或推广。

本软件由版权持有者和贡献者按“原样”提供，不作任何明示或暗示的保证，包括但不限于对适销性和特定用途适用性的暗示保证。在任何情况下，版权持有者或贡献者均不对因使用本软件而引起的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用、数据或利润的损失，或业务中断）承担责任，无论责任主张基于合同、严格责任或侵权行为（包括过失或其他），即使已被告知可能发生此类损害。

## BSD 四条款许可证（BSD 4-Clause “Original” or “Old” License，BSD-4-Clause）

BSD 四条款许可证是 BSD 许可证的原始版本，具有较多限制条件。BSD 四条款许可证即原始的 BSD 许可证，目前不被 OSI 认可。此许可证带有广告条款，要求在所有提及本软件功能或用途的广告材料中声明使用了原作者的产品（参见下文第 3 条）。

```text
Copyright (c) <年份> <持有者>. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software must display the following acknowledgement:
This product includes software developed by the organization.
4. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY COPYRIGHT HOLDER "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

版权所有 <年份> <所有者>。保留所有权利。

在满足以下条件的前提下，允许在源代码和二进制形式中重新分发和使用本软件，无论是否经过修改：

1. 源代码的再发布必须保留上述版权声明、本条件列表以及以下免责声明。
2. 二进制形式的再发布必须在随附的文档和/或其他材料中复制上述版权声明、本条件列表以及以下免责声明。
3. 所有提及本软件功能或用途的广告材料中必须包含以下致谢声明：本产品包含由该组织开发的软件。
4. 未经事先书面许可，不得使用版权持有者及其贡献者的姓名为源自本软件的产品背书或推广。

本软件由版权持有者按“原样”提供，不作任何明示或暗示的保证，包括但不限于对适销性和特定用途适用性的暗示保证。在任何情况下，版权持有者均不对因使用本软件而引起的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用、数据或利润的损失，或业务中断）承担责任，无论责任主张基于合同、严格责任或侵权行为（包括过失或其他），即使已被告知可能发生此类损害。

## 课后习题

1. 选取一个真实的开源项目（如某个 FreeBSD Ports 中的软件），追踪其许可证演变历史，分析从 BSD-2-Clause 到 BSD-3-Clause 或反之的变更原因，并思考该变更如何调整了用户与开发者之间的权力关系。

2. 构建一个最小化的包含 BSD 零条款与 GPLv3 代码的软件组合，分析这种许可证混合在实际分发中可能产生的约束，并思考为什么 BSD 许可证的非 copyleft 特性会形成与 copyleft 许可证截然不同的生态权力结构。
