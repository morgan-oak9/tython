// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_kms_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleKmsBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_kms_bundle.proto</summary>
  public static partial class GcpGoogleKmsBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_kms_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleKmsBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch9nY3AvZ2NwX2dvb2dsZV9rbXNfYnVuZGxlLnByb3RvEiFvYWs5LnR5dGhv",
            "bi5nY3AuZ29vZ2xlX2ttc19idW5kbGUaE3NoYXJlZC9zaGFyZWQucHJvdG8a",
            "EWdjcC9nY3Bfa21zLnByb3RvIuMFCglHb29nbGVLbXMSOQoOa21zX2NyeXB0",
            "b19rZXkYASADKAsyIS5vYWs5LnR5dGhvbi5nY3Aua21zLkttc0NyeXB0b0tl",
            "eRJPChprbXNfY3J5cHRvX2tleV9pYW1fYmluZGluZxgCIAMoCzIrLm9hazku",
            "dHl0aG9uLmdjcC5rbXMuS21zQ3J5cHRvS2V5SWFtQmluZGluZxJNChlrbXNf",
            "Y3J5cHRvX2tleV9pYW1fbWVtYmVyGAMgAygLMioub2FrOS50eXRob24uZ2Nw",
            "Lmttcy5LbXNDcnlwdG9LZXlJYW1NZW1iZXISTQoZa21zX2NyeXB0b19rZXlf",
            "aWFtX3BvbGljeRgEIAMoCzIqLm9hazkudHl0aG9uLmdjcC5rbXMuS21zQ3J5",
            "cHRvS2V5SWFtUG9saWN5EjUKDGttc19rZXlfcmluZxgFIAEoCzIfLm9hazku",
            "dHl0aG9uLmdjcC5rbXMuS21zS2V5UmluZxJLChhrbXNfa2V5X3JpbmdfaWFt",
            "X2JpbmRpbmcYBiADKAsyKS5vYWs5LnR5dGhvbi5nY3Aua21zLkttc0tleVJp",
            "bmdJYW1CaW5kaW5nEkkKF2ttc19rZXlfcmluZ19pYW1fbWVtYmVyGAcgAygL",
            "Migub2FrOS50eXRob24uZ2NwLmttcy5LbXNLZXlSaW5nSWFtTWVtYmVyEkkK",
            "F2ttc19rZXlfcmluZ19pYW1fcG9saWN5GAggAygLMigub2FrOS50eXRob24u",
            "Z2NwLmttcy5LbXNLZXlSaW5nSWFtUG9saWN5EkkKF2ttc19rZXlfcmluZ19p",
            "bXBvcnRfam9iGAkgAygLMigub2FrOS50eXRob24uZ2NwLmttcy5LbXNLZXlS",
            "aW5nSW1wb3J0Sm9iEkcKFWttc19zZWNyZXRfY2lwaGVydGV4dBgKIAEoCzIo",
            "Lm9hazkudHl0aG9uLmdjcC5rbXMuS21zU2VjcmV0Q2lwaGVydGV4dGIGcHJv",
            "dG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.Kms.GcpKmsReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleKmsBundle.GoogleKms), global::Oak9.Tython.Gcp.GoogleKmsBundle.GoogleKms.Parser, new[]{ "KmsCryptoKey", "KmsCryptoKeyIamBinding", "KmsCryptoKeyIamMember", "KmsCryptoKeyIamPolicy", "KmsKeyRing", "KmsKeyRingIamBinding", "KmsKeyRingIamMember", "KmsKeyRingIamPolicy", "KmsKeyRingImportJob", "KmsSecretCiphertext" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleKms : pb::IMessage<GoogleKms>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleKms> _parser = new pb::MessageParser<GoogleKms>(() => new GoogleKms());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleKms> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleKmsBundle.GcpGoogleKmsBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleKms() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleKms(GoogleKms other) : this() {
      kmsCryptoKey_ = other.kmsCryptoKey_.Clone();
      kmsCryptoKeyIamBinding_ = other.kmsCryptoKeyIamBinding_.Clone();
      kmsCryptoKeyIamMember_ = other.kmsCryptoKeyIamMember_.Clone();
      kmsCryptoKeyIamPolicy_ = other.kmsCryptoKeyIamPolicy_.Clone();
      kmsKeyRing_ = other.kmsKeyRing_ != null ? other.kmsKeyRing_.Clone() : null;
      kmsKeyRingIamBinding_ = other.kmsKeyRingIamBinding_.Clone();
      kmsKeyRingIamMember_ = other.kmsKeyRingIamMember_.Clone();
      kmsKeyRingIamPolicy_ = other.kmsKeyRingIamPolicy_.Clone();
      kmsKeyRingImportJob_ = other.kmsKeyRingImportJob_.Clone();
      kmsSecretCiphertext_ = other.kmsSecretCiphertext_ != null ? other.kmsSecretCiphertext_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleKms Clone() {
      return new GoogleKms(this);
    }

    /// <summary>Field number for the "kms_crypto_key" field.</summary>
    public const int KmsCryptoKeyFieldNumber = 1;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsCryptoKey> _repeated_kmsCryptoKey_codec
        = pb::FieldCodec.ForMessage(10, global::Oak9.Tython.Gcp.Kms.KmsCryptoKey.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKey> kmsCryptoKey_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKey>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKey> KmsCryptoKey {
      get { return kmsCryptoKey_; }
    }

    /// <summary>Field number for the "kms_crypto_key_iam_binding" field.</summary>
    public const int KmsCryptoKeyIamBindingFieldNumber = 2;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamBinding> _repeated_kmsCryptoKeyIamBinding_codec
        = pb::FieldCodec.ForMessage(18, global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamBinding.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamBinding> kmsCryptoKeyIamBinding_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamBinding>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamBinding> KmsCryptoKeyIamBinding {
      get { return kmsCryptoKeyIamBinding_; }
    }

    /// <summary>Field number for the "kms_crypto_key_iam_member" field.</summary>
    public const int KmsCryptoKeyIamMemberFieldNumber = 3;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamMember> _repeated_kmsCryptoKeyIamMember_codec
        = pb::FieldCodec.ForMessage(26, global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamMember.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamMember> kmsCryptoKeyIamMember_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamMember>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamMember> KmsCryptoKeyIamMember {
      get { return kmsCryptoKeyIamMember_; }
    }

    /// <summary>Field number for the "kms_crypto_key_iam_policy" field.</summary>
    public const int KmsCryptoKeyIamPolicyFieldNumber = 4;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamPolicy> _repeated_kmsCryptoKeyIamPolicy_codec
        = pb::FieldCodec.ForMessage(34, global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamPolicy.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamPolicy> kmsCryptoKeyIamPolicy_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamPolicy>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsCryptoKeyIamPolicy> KmsCryptoKeyIamPolicy {
      get { return kmsCryptoKeyIamPolicy_; }
    }

    /// <summary>Field number for the "kms_key_ring" field.</summary>
    public const int KmsKeyRingFieldNumber = 5;
    private global::Oak9.Tython.Gcp.Kms.KmsKeyRing kmsKeyRing_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Kms.KmsKeyRing KmsKeyRing {
      get { return kmsKeyRing_; }
      set {
        kmsKeyRing_ = value;
      }
    }

    /// <summary>Field number for the "kms_key_ring_iam_binding" field.</summary>
    public const int KmsKeyRingIamBindingFieldNumber = 6;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamBinding> _repeated_kmsKeyRingIamBinding_codec
        = pb::FieldCodec.ForMessage(50, global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamBinding.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamBinding> kmsKeyRingIamBinding_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamBinding>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamBinding> KmsKeyRingIamBinding {
      get { return kmsKeyRingIamBinding_; }
    }

    /// <summary>Field number for the "kms_key_ring_iam_member" field.</summary>
    public const int KmsKeyRingIamMemberFieldNumber = 7;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamMember> _repeated_kmsKeyRingIamMember_codec
        = pb::FieldCodec.ForMessage(58, global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamMember.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamMember> kmsKeyRingIamMember_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamMember>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamMember> KmsKeyRingIamMember {
      get { return kmsKeyRingIamMember_; }
    }

    /// <summary>Field number for the "kms_key_ring_iam_policy" field.</summary>
    public const int KmsKeyRingIamPolicyFieldNumber = 8;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamPolicy> _repeated_kmsKeyRingIamPolicy_codec
        = pb::FieldCodec.ForMessage(66, global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamPolicy.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamPolicy> kmsKeyRingIamPolicy_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamPolicy>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingIamPolicy> KmsKeyRingIamPolicy {
      get { return kmsKeyRingIamPolicy_; }
    }

    /// <summary>Field number for the "kms_key_ring_import_job" field.</summary>
    public const int KmsKeyRingImportJobFieldNumber = 9;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Gcp.Kms.KmsKeyRingImportJob> _repeated_kmsKeyRingImportJob_codec
        = pb::FieldCodec.ForMessage(74, global::Oak9.Tython.Gcp.Kms.KmsKeyRingImportJob.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingImportJob> kmsKeyRingImportJob_ = new pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingImportJob>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Gcp.Kms.KmsKeyRingImportJob> KmsKeyRingImportJob {
      get { return kmsKeyRingImportJob_; }
    }

    /// <summary>Field number for the "kms_secret_ciphertext" field.</summary>
    public const int KmsSecretCiphertextFieldNumber = 10;
    private global::Oak9.Tython.Gcp.Kms.KmsSecretCiphertext kmsSecretCiphertext_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Kms.KmsSecretCiphertext KmsSecretCiphertext {
      get { return kmsSecretCiphertext_; }
      set {
        kmsSecretCiphertext_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleKms);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleKms other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!kmsCryptoKey_.Equals(other.kmsCryptoKey_)) return false;
      if(!kmsCryptoKeyIamBinding_.Equals(other.kmsCryptoKeyIamBinding_)) return false;
      if(!kmsCryptoKeyIamMember_.Equals(other.kmsCryptoKeyIamMember_)) return false;
      if(!kmsCryptoKeyIamPolicy_.Equals(other.kmsCryptoKeyIamPolicy_)) return false;
      if (!object.Equals(KmsKeyRing, other.KmsKeyRing)) return false;
      if(!kmsKeyRingIamBinding_.Equals(other.kmsKeyRingIamBinding_)) return false;
      if(!kmsKeyRingIamMember_.Equals(other.kmsKeyRingIamMember_)) return false;
      if(!kmsKeyRingIamPolicy_.Equals(other.kmsKeyRingIamPolicy_)) return false;
      if(!kmsKeyRingImportJob_.Equals(other.kmsKeyRingImportJob_)) return false;
      if (!object.Equals(KmsSecretCiphertext, other.KmsSecretCiphertext)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= kmsCryptoKey_.GetHashCode();
      hash ^= kmsCryptoKeyIamBinding_.GetHashCode();
      hash ^= kmsCryptoKeyIamMember_.GetHashCode();
      hash ^= kmsCryptoKeyIamPolicy_.GetHashCode();
      if (kmsKeyRing_ != null) hash ^= KmsKeyRing.GetHashCode();
      hash ^= kmsKeyRingIamBinding_.GetHashCode();
      hash ^= kmsKeyRingIamMember_.GetHashCode();
      hash ^= kmsKeyRingIamPolicy_.GetHashCode();
      hash ^= kmsKeyRingImportJob_.GetHashCode();
      if (kmsSecretCiphertext_ != null) hash ^= KmsSecretCiphertext.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      kmsCryptoKey_.WriteTo(output, _repeated_kmsCryptoKey_codec);
      kmsCryptoKeyIamBinding_.WriteTo(output, _repeated_kmsCryptoKeyIamBinding_codec);
      kmsCryptoKeyIamMember_.WriteTo(output, _repeated_kmsCryptoKeyIamMember_codec);
      kmsCryptoKeyIamPolicy_.WriteTo(output, _repeated_kmsCryptoKeyIamPolicy_codec);
      if (kmsKeyRing_ != null) {
        output.WriteRawTag(42);
        output.WriteMessage(KmsKeyRing);
      }
      kmsKeyRingIamBinding_.WriteTo(output, _repeated_kmsKeyRingIamBinding_codec);
      kmsKeyRingIamMember_.WriteTo(output, _repeated_kmsKeyRingIamMember_codec);
      kmsKeyRingIamPolicy_.WriteTo(output, _repeated_kmsKeyRingIamPolicy_codec);
      kmsKeyRingImportJob_.WriteTo(output, _repeated_kmsKeyRingImportJob_codec);
      if (kmsSecretCiphertext_ != null) {
        output.WriteRawTag(82);
        output.WriteMessage(KmsSecretCiphertext);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      kmsCryptoKey_.WriteTo(ref output, _repeated_kmsCryptoKey_codec);
      kmsCryptoKeyIamBinding_.WriteTo(ref output, _repeated_kmsCryptoKeyIamBinding_codec);
      kmsCryptoKeyIamMember_.WriteTo(ref output, _repeated_kmsCryptoKeyIamMember_codec);
      kmsCryptoKeyIamPolicy_.WriteTo(ref output, _repeated_kmsCryptoKeyIamPolicy_codec);
      if (kmsKeyRing_ != null) {
        output.WriteRawTag(42);
        output.WriteMessage(KmsKeyRing);
      }
      kmsKeyRingIamBinding_.WriteTo(ref output, _repeated_kmsKeyRingIamBinding_codec);
      kmsKeyRingIamMember_.WriteTo(ref output, _repeated_kmsKeyRingIamMember_codec);
      kmsKeyRingIamPolicy_.WriteTo(ref output, _repeated_kmsKeyRingIamPolicy_codec);
      kmsKeyRingImportJob_.WriteTo(ref output, _repeated_kmsKeyRingImportJob_codec);
      if (kmsSecretCiphertext_ != null) {
        output.WriteRawTag(82);
        output.WriteMessage(KmsSecretCiphertext);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      size += kmsCryptoKey_.CalculateSize(_repeated_kmsCryptoKey_codec);
      size += kmsCryptoKeyIamBinding_.CalculateSize(_repeated_kmsCryptoKeyIamBinding_codec);
      size += kmsCryptoKeyIamMember_.CalculateSize(_repeated_kmsCryptoKeyIamMember_codec);
      size += kmsCryptoKeyIamPolicy_.CalculateSize(_repeated_kmsCryptoKeyIamPolicy_codec);
      if (kmsKeyRing_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(KmsKeyRing);
      }
      size += kmsKeyRingIamBinding_.CalculateSize(_repeated_kmsKeyRingIamBinding_codec);
      size += kmsKeyRingIamMember_.CalculateSize(_repeated_kmsKeyRingIamMember_codec);
      size += kmsKeyRingIamPolicy_.CalculateSize(_repeated_kmsKeyRingIamPolicy_codec);
      size += kmsKeyRingImportJob_.CalculateSize(_repeated_kmsKeyRingImportJob_codec);
      if (kmsSecretCiphertext_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(KmsSecretCiphertext);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleKms other) {
      if (other == null) {
        return;
      }
      kmsCryptoKey_.Add(other.kmsCryptoKey_);
      kmsCryptoKeyIamBinding_.Add(other.kmsCryptoKeyIamBinding_);
      kmsCryptoKeyIamMember_.Add(other.kmsCryptoKeyIamMember_);
      kmsCryptoKeyIamPolicy_.Add(other.kmsCryptoKeyIamPolicy_);
      if (other.kmsKeyRing_ != null) {
        if (kmsKeyRing_ == null) {
          KmsKeyRing = new global::Oak9.Tython.Gcp.Kms.KmsKeyRing();
        }
        KmsKeyRing.MergeFrom(other.KmsKeyRing);
      }
      kmsKeyRingIamBinding_.Add(other.kmsKeyRingIamBinding_);
      kmsKeyRingIamMember_.Add(other.kmsKeyRingIamMember_);
      kmsKeyRingIamPolicy_.Add(other.kmsKeyRingIamPolicy_);
      kmsKeyRingImportJob_.Add(other.kmsKeyRingImportJob_);
      if (other.kmsSecretCiphertext_ != null) {
        if (kmsSecretCiphertext_ == null) {
          KmsSecretCiphertext = new global::Oak9.Tython.Gcp.Kms.KmsSecretCiphertext();
        }
        KmsSecretCiphertext.MergeFrom(other.KmsSecretCiphertext);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            kmsCryptoKey_.AddEntriesFrom(input, _repeated_kmsCryptoKey_codec);
            break;
          }
          case 18: {
            kmsCryptoKeyIamBinding_.AddEntriesFrom(input, _repeated_kmsCryptoKeyIamBinding_codec);
            break;
          }
          case 26: {
            kmsCryptoKeyIamMember_.AddEntriesFrom(input, _repeated_kmsCryptoKeyIamMember_codec);
            break;
          }
          case 34: {
            kmsCryptoKeyIamPolicy_.AddEntriesFrom(input, _repeated_kmsCryptoKeyIamPolicy_codec);
            break;
          }
          case 42: {
            if (kmsKeyRing_ == null) {
              KmsKeyRing = new global::Oak9.Tython.Gcp.Kms.KmsKeyRing();
            }
            input.ReadMessage(KmsKeyRing);
            break;
          }
          case 50: {
            kmsKeyRingIamBinding_.AddEntriesFrom(input, _repeated_kmsKeyRingIamBinding_codec);
            break;
          }
          case 58: {
            kmsKeyRingIamMember_.AddEntriesFrom(input, _repeated_kmsKeyRingIamMember_codec);
            break;
          }
          case 66: {
            kmsKeyRingIamPolicy_.AddEntriesFrom(input, _repeated_kmsKeyRingIamPolicy_codec);
            break;
          }
          case 74: {
            kmsKeyRingImportJob_.AddEntriesFrom(input, _repeated_kmsKeyRingImportJob_codec);
            break;
          }
          case 82: {
            if (kmsSecretCiphertext_ == null) {
              KmsSecretCiphertext = new global::Oak9.Tython.Gcp.Kms.KmsSecretCiphertext();
            }
            input.ReadMessage(KmsSecretCiphertext);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            kmsCryptoKey_.AddEntriesFrom(ref input, _repeated_kmsCryptoKey_codec);
            break;
          }
          case 18: {
            kmsCryptoKeyIamBinding_.AddEntriesFrom(ref input, _repeated_kmsCryptoKeyIamBinding_codec);
            break;
          }
          case 26: {
            kmsCryptoKeyIamMember_.AddEntriesFrom(ref input, _repeated_kmsCryptoKeyIamMember_codec);
            break;
          }
          case 34: {
            kmsCryptoKeyIamPolicy_.AddEntriesFrom(ref input, _repeated_kmsCryptoKeyIamPolicy_codec);
            break;
          }
          case 42: {
            if (kmsKeyRing_ == null) {
              KmsKeyRing = new global::Oak9.Tython.Gcp.Kms.KmsKeyRing();
            }
            input.ReadMessage(KmsKeyRing);
            break;
          }
          case 50: {
            kmsKeyRingIamBinding_.AddEntriesFrom(ref input, _repeated_kmsKeyRingIamBinding_codec);
            break;
          }
          case 58: {
            kmsKeyRingIamMember_.AddEntriesFrom(ref input, _repeated_kmsKeyRingIamMember_codec);
            break;
          }
          case 66: {
            kmsKeyRingIamPolicy_.AddEntriesFrom(ref input, _repeated_kmsKeyRingIamPolicy_codec);
            break;
          }
          case 74: {
            kmsKeyRingImportJob_.AddEntriesFrom(ref input, _repeated_kmsKeyRingImportJob_codec);
            break;
          }
          case 82: {
            if (kmsSecretCiphertext_ == null) {
              KmsSecretCiphertext = new global::Oak9.Tython.Gcp.Kms.KmsSecretCiphertext();
            }
            input.ReadMessage(KmsSecretCiphertext);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code